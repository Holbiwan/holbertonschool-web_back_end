/* eslint-disable */

const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  // Tests pour SUM
  it('should return the sum of rounded numbers (SUM)', () => {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
    expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
    expect(calculateNumber('SUM', -1.3, -4.5)).to.equal(-5);
    expect(calculateNumber('SUM', 0.4, 0.6)).to.equal(1);
  });

  // Tests pour SUBTRACT
  it('should return the difference of rounded numbers (SUBTRACT)', () => {
    expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
    expect(calculateNumber('SUBTRACT', 1.2, 3.7)).to.equal(-3);
    expect(calculateNumber('SUBTRACT', 1.5, 3.7)).to.equal(-2);
    expect(calculateNumber('SUBTRACT', -1.3, -4.5)).to.equal(3);
    expect(calculateNumber('SUBTRACT', 0.4, 0.6)).to.equal(-1);
  });

  // Tests pour DIVIDE
  it('should return the division of rounded numbers (DIVIDE)', () => {
    expect(calculateNumber('DIVIDE', 1, 3)).to.equal(0.3333333333333333);
    expect(calculateNumber('DIVIDE', 1.2, 3.7)).to.equal(0.25);
    expect(calculateNumber('DIVIDE', 1.5, 3.7)).to.equal(0.5);
    expect(calculateNumber('DIVIDE', -1.3, -4.5)).to.equal(0.25);
    expect(calculateNumber('DIVIDE', 0.4, 0.2)).to.equal(2);
  });

  it('should return Error when dividing by 0 (DIVIDE)', () => {
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  });
});
