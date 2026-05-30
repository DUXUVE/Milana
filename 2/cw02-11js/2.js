function getExclamated(text) {
  if (!text) {
    return text;
  }
  if (text === "") {
    return "";
  }
  return text + "!";
}

function exclamate(text) {
  console.log(getExclamated(text));
}

exclamate("Hello");
console.log(getExclamated("Goodbye") === "Goodbye!");
console.log(getExclamated("") === "");
console.log(getExclamated(null) === null);
console.log(typeof getExclamated(undefined) === 'undefined');
