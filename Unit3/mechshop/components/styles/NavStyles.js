import styled from 'styled-components';

const Nav = styled.ul`
    margin: 0;
    padding: 0;
    display: flex;
    justify-self: end;
    a,
    button {
        cursor: pointer;
        text-decoration: none;
        padding: 1rem 3rem;
        display: flex;
        align-items: center;
        position: relative;
        text-transform: uppercase;
        font-weight: 900;
        font-size: 16px;
        border: 0;
        color: ${props => props.theme.color};
    }
`;

export default Nav;