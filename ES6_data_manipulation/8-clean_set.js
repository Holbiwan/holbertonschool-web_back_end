const cleanSet = (set, startString) => {
  if (startString === '') {
    return '';
  }
  const newSet = [];
  set.forEach((element) => {
    if (element.startsWith(startString)) {
      newSet.push(element.slice(startString.length));
    }
  });
  return newSet.join('-');
}
export default cleanSet;
