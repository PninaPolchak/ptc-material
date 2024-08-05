import { render, fireEvent } from '@testing-library/react';
import React from 'react';
import App from './App';

test('Button click updates the display correctly', () => {
  const { getByText } = render(<App />);
  
  const button5 = getByText('13');
  fireEvent.click(button5);

  const buttonPlus = getByText('+');
  fireEvent.click(buttonPlus);

  const button3 = getByText('2');
  fireEvent.click(button3);

  const buttonEquals = getByText('=');
  fireEvent.click(buttonEquals);

  const result = getByText('15');
  expect(result).toBeInTheDocument();
});