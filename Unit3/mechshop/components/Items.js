import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import Item from './Item';
import client from '../utils/api-client';

const Center = styled.div`
    text-align: center;
`;

const ItemsList = styled.div`
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-gap: 60px;
    max-width: ${props => props.theme.maxWidth};
    margin: 0 auto;
`;

function Items() {
    const [items, setItems] = useState([]);

    useEffect(() => {
        client('items', { method: 'GET' })
        .then(({ payload }) => setItems(payload.items))
        .catch(e => console.log(e));
    }, []);

    return (
        <Center>
            <ItemsList>
                { items.map(item => (
                    <Item item={item} key={item.id}/>
                )) }
            </ItemsList>
        </Center>
    );
}

export default Items;