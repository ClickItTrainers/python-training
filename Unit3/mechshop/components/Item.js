import ItemStyles from './styles/ItemStyles';

function Item(props) {
    const { item } = props;

    return (
        <ItemStyles>
            <img src="/static/gnome.jpeg" alt="Image"/>
            <h3>{ item.title }</h3>
            <p>{ item.description }</p>
        </ItemStyles>
    );
}

export default Item;