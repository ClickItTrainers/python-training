import styled from 'styled-components';
import Link from 'next/link';
import Nav from './Nav';

const StyledHeader = styled.header`
    .bar {
        border-bottom: 1px solid #394047;
        display: grid;
        grid-template-columns: auto 1fr;
        justify-content: space-between;
        align-items: stretch;
        @media (max-width: 1300px) {
            grid-template-colums: 1fr;
            justify-content: center;
        }
    }
`;

const Logo = styled.h1`
    font-family: 'Staatliches';
    font-size: 2rem;
    margin-left: 2rem;
    position: relative;
    z-index: 2;
    a {
        padding: 0.5rem 1rem;
        color: ${props => props.theme.secondaryColor};
        text-transform: uppercase;
        text-decoration: none;
    }
    @media (max-width: 1300px) {
        margin: 0;
        text-align: center;
    }
`;

const Header = () => (
    <StyledHeader>
        <div className="bar">
            <Logo>
                <Link href="/">
                    <a>_MECHSHOP_</a>
                </Link>
            </Logo>
            <Nav/>
        </div>
    </StyledHeader>
);

export default Header;