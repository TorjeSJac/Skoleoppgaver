//alt av javascript er skrevet med ChatGPT
function addToResult(value) {
    document.getElementById('result').innerText += value;
  }

  function calculate() {
    let result = document.getElementById('result').innerText;
    let calculation;
    try {
      calculation = eval(result);
    } catch (error) {
      calculation = 'Error';
    }
    document.getElementById('result').innerText = calculation;
  }

  function clearResult() {
    document.getElementById('result').innerText = '';
  }