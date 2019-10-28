import NavStyles from './styles/NavStyles';
import Link from 'next/link';

function Nav(props) {
    return (
        <NavStyles>
            <Link href="/sell">
                <a>Sell</a>
            </Link>
            <Link href="/signup">
                <a>Sign In</a>
            </Link>
            <Link href="/signup">
                <a>Sign Up</a>
            </Link>
        </NavStyles>
    );
}

export default Nav;