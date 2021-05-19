import { useState } from "react";
import { Button, Layout, Typography } from "antd";

import "./Contribute.styles.scss";

const { Content } = Layout;
const { Title } = Typography;

const text = `Lorem ipsum dolor sit, amet consectetur adipisicing elit. Officiisquo esse ex dolore officia quis consequuntur, nisi obcaecatitotam, labore illum. Inventore porro fugiat at, fugit quam temporaperspiciatis suscipit.`;

const Contribute = () => {
  const [state, setstate] = useState();

  return (
    <Content className="contribute-content">
      <div className="landing">
        <div className="overlay">
          <div className="contribute-text">
            <Title level={2} className="contribute-text__header">
              Help us Build
            </Title>
            <Typography className="contribute-text__para">{text}</Typography>
          </div>
          <Button
            type="primary"
            shape="round"
            className="contribute-button"
            // size="large"
            onClick={() => console.log("clicked")}
          >
            Contribute
          </Button>
        </div>
      </div>
      <div className="contribution">
        <Typography>Contribute here</Typography>
      </div>
    </Content>
  );
};

export default Contribute;
