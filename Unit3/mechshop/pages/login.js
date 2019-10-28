import React, { useState } from 'react';
import { useRouter } from 'next/router';
import Form from '../components/styles/Form';
import client from '../utils/api-client';
import { storeToken } from '../utils/auth';

export default function Login(props) {
    const router = useRouter();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    function handleSubmit(e) {
        e.preventDefault();

        client('signin', { 
            method: 'POST',
            body: { email, password }
        })
        .then(({payload}) => {
            storeToken(payload.token);
            router.push('/');
        })
        .catch(e => console.log(e));
    }

    return (
        <div>
            <Form onSubmit={handleSubmit}>
                <label htmlFor="email">
                    Email:
                    <input 
                        type="email"
                        name="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </label>
                <label htmlFor="password">
                    Password:
                    <input 
                        type="password"
                        name="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </label>

                <button type="submit">Log In!</button>
            </Form>
        </div>
    )
}