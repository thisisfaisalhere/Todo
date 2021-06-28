import { Link, useHistory } from "react-router-dom";
import { Layout, Menu, Typography } from "antd";
import "./Navbar.styles.scss";

const { Header } = Layout;

const Navbar = () => {
  const history = useHistory();

  return (
    <Header className="navbar">
      <div className="brand" onClick={() => history.replace("/")}>
        <div className="logo" />
        <Typography className="brand-name">dyeSee</Typography>
      </div>
      <Menu theme="dark" mode="horizontal" defaultSelectedKeys={["1"]}>
        <Menu.Item key="1">
          <Link to="/">Home</Link>
        </Menu.Item>
        <Menu.Item key="2">
          <Link to="/someLink">Some Page</Link>
        </Menu.Item>
      </Menu>
    </Header>
  );
};

export default Navbar;
