import Items from '../components/Items';
import { withAuth } from '../utils/auth';

function Home(props) {
    console.log(props);

    return (
        <div>
            <Items />            
        </div>
    );
}

export default withAuth(Home);