export default function client(endpoint, { body, ...customConfig } = {}) {
    const headers = {
        'Content-Type': 'application/json'
    };

    const config = {
        ...customConfig, 
        headers: {
            ...headers,
            ...customConfig.headers
        }
    }

    if(body) {
        config.body = JSON.stringify(body); 
    }
    
    return window
        .fetch(`${process.env.apiEndpoint}/${endpoint}`, config)
        .then(async response => {
            if(response.ok) return response.json();

            return Promise.reject(await response.json());
        });

}