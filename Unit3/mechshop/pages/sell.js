import React, { useReducer } from 'react';
import Form from '../components/styles/Form';
import client from '../utils/api-client';
import { useRouter } from 'next/router';

export default function Sell(props) {
    const router = useRouter();
    const [state, setState] = useReducer(
        (s, a) => ({ ...s, ...a }),
        {
            title: '',
            price: 0,
            description: '',
            image: '',
        }
    )

    function handleChange(e) {
        const { name, type, value } = e.target;
        setState({ [name]: value });
    }

    function handleSubmit(e) {
        e.preventDefault();

        let form = new FormData();

        //Fill the form with the given data
        Object.keys(state).forEach((key) => form.append(key, state[key]));

        client('items', {
            method: 'POST',
            body: state
        })
        .then(({ payload }) => {
            /*router.push({
                pathname: '/item',
                query: { id: payload.itemId }
            });*/
        })
    }

    return (
        <Form onSubmit={handleSubmit}>
            <label htmlFor="title">
                Title:
                <input 
                    type="text"
                    name="title"
                    value={state.title}
                    onChange={handleChange}
                    placeholder="Please enter a title"
                    required
                />
            </label>
            <label htmlFor="price">
                Price:
                <input 
                    type="number"
                    name="price"
                    value={state.price}
                    onChange={handleChange}
                    placeholder="0.00"
                    required
                />
            </label>
            <label htmlFor="description">
                Description:
                <textarea 
                    name="description"
                    value={state.description}
                    onChange={handleChange}
                    placeholder="Please enter a description"
                    required
                />
            </label>

            <label>
                Image:
                <input
                    type="file"
                    name="image"
                    required
                />
            </label>

            <button type="submit">Create</button>
        </Form>
    );
}