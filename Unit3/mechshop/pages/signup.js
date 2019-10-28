import { useState } from 'react';
import { useRouter } from 'next/router';
import Form from '../components/styles/Form';
import client from '../utils/api-client';
import { storeToken } from '../utils/auth';

function SignUp() {
    const router = useRouter();
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    function handleSubmit(e) {
        e.preventDefault();

        client('signup', { 
            method: 'POST',
            body: { first_name: firstName, last_name: lastName, email, password },
        })
        .then(({ payload }) => {
            storeToken(payload.token);
            router.push('/');
        })
        .catch(err => {

        });
    }

    return (
        <Form onSubmit={handleSubmit}>
            <h3>Sign Up!</h3>
            <label htmlFor="first_name">First Name:
                <input
                    type="text"
                    value={firstName}
                    onChange={(e) => setFirstName(e.target.value)}
                />
            </label>

            <label htmlFor="last_name">Last Name:
                <input 
                    type="text"
                    value={lastName}
                    onChange={(e) => setLastName(e.target.value)}
                />
            </label>

            <label htmlFor="email">Email:
                <input 
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
            </label>

            <label htmlFor="password">Password: 
                <input 
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
            </label>
            <button type="submit">Sign Up</button>
        </Form>
    )
}

export default SignUp;