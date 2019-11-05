import Items from '../components/Items';
import { withAuth } from '../utils/auth';

function Home(props) {
    return (
        <div>
            <h2 style={{ textAlign: 'center' }}>Featured products</h2>
            <Items />            
        </div>
    );
}

export default withAuth(Home);