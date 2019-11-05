import NavStyles from './styles/NavStyles';
import Link from 'next/link';

function Nav(props) {
    return (
        <NavStyles>
            <Link href="/sell">
                <a>Sell</a>
            </Link>
            <Link href="/me">
                <a>Account</a>
            </Link>
            <Link href="/signout">
                <a>Sign Out</a>
            </Link>
        </NavStyles>
    );
}

export default Nav;