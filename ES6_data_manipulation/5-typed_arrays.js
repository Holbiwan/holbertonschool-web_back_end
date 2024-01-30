const createInt8TypedArray = (length, position, value) => {
    if (position < 0 || position >= length) throw new Error('Position outside range');
    const view = new DataView(new ArrayBuffer(length));
    view.setInt8(position, value);
    return view;
  };
  
  export default createInt8TypedArray;
  