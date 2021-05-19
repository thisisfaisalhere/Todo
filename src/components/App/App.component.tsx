import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Navbar from "../Navbar/Navbar.component";
import Home from "../pages/Home/Home.component";
import Contribute from "../pages/Contribute/Contribute.component";

import "antd/dist/antd.css";

function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/contribute" component={Contribute} />
      </Switch>
    </Router>
  );
}

export default App;
