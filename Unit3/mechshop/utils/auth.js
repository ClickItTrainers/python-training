import cookie from 'js-cookie';
import nextCookie from 'next-cookies';
import Router from 'next/router';

export function storeToken(token) {
    cookie.set('_mechshop_token_', token, { expires: 1 });
    return token;
}

export function getToken() {
    return cookie.get('_mechshop_token_')
}

export const authenticate = ctx => {
    const { _mechshop_token_ } = nextCookie(ctx);

    /** If ctx.req exists it means we are still on the server */
    if(ctx.req && !_mechshop_token_) {
        ctx.res.writeHead(302, { Location: '/login' });
        ctx.res.end();
    }

    // We already checked on the server, this is only for client-side.
    if(!_mechshop_token_) {
        Router.push('/login');
    }

    return _mechshop_token_;
}

export const withAuth = WrappedComponent => {
    const Wrapper = props => {
        return <WrappedComponent {...props}/>
    }

    Wrapper.getInitialProps = async ctx => {
        const token = authenticate(ctx);

        const componentProps = 
            WrappedComponent.getInitialProps &&
            (await WrappedComponent.getInitialProps(ctx));

        return { 
            ...componentProps,
            user: { token }
        };
    }

    return Wrapper;
}