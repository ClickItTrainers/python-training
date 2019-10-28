import styled from 'styled-components';

const Form = styled.form`
    padding: 20px;
    font-size: 1em;
    line-height: 1.5;
    font-weight: 600;
    label {
        display: block;
        margin-bottom: 1em;
    }
    input,
    textarea,
    select {
        width: 100%;
        padding: 1rem;
        font-size: 1em;
        background: ${props => props.theme.mainColor};
        border: 1px solid ${props => props.theme.color};
        color: #a797a7;

        &:focus {
            outline: 0;
            border: 1px solid blue;
        }
    }
    button,
    input[type="submit"] {
        width: auto;
        background: ${props => props.theme.mainColor};
        border: 1.5px solid #b5656d;
        border-radius: 4px;
        color: white;
        font-size: 1em;
        font-weight: 600;
        padding: 0.5rem 1.2rem;

        &:hover {
            background: #b5656d;
        }
    }
`;

export default Form;