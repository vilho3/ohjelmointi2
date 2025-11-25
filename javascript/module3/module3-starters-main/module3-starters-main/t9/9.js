let result = 0;

const button = document.querySelector('#start');

button.addEventListener('click', function() {
  const input = document.querySelector('#calculation').value;
  const calculation = input.split('');

  const num1 = parseInt(calculation[0]);
  const num2 = parseInt(calculation[2]);

  if (calculation.includes('+')) {
    result = num1 + num2;
  } else if (calculation.includes('-')) {
    result = num1 - num2;
  } else if (calculation.includes('*')) {
    result = num1 * num2;
  } else if (calculation.includes('/')) {
    result = num1 / num2;
  }

  let p = document.querySelector('#result');
  p.textContent = result;
});
