export default function taskBlock(trueOrFalse) {
    const task = false;
    const task2 = true;
  
    // eslint-disable-next-line
    if (trueOrFalse) {
      const task = true;
      const task2 = false;
    }
    // eslint-disable-no-unused-vars
  
    return [task, task2];
}