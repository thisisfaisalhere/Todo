import { render, screen } from "@testing-library/react";
import Navbar from "./Navbar.component";

test("renders learn react link", () => {
  render(<Navbar />);

  // Todo: write test
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
