import styled from 'styled-components';

const Item = styled.div`
    background: #394047;
    color: ${props => props.theme.color};
    border: 1px solid ${props => props.theme.mainColor};
    border-radius: 4px;
    position: relative;
    display: flex;
    flex-direction: column;
    img {
        width: 100%;
        height: 166px;
        object-fit: cover;
        padding: 5px;
        border-radius: 4px;
    }
    h3 {
        font-size: 18px;
        line-height: 2;
        margin: 0;
    }
    p {
        font-size: 12px;
        line-height: 2;
        font-weight: 300;
        flex-grow: 1;
        padding: 0 3rem;
        margin-top: 5px;
        margin-bottom: 0;
    }
`;

export default Item;