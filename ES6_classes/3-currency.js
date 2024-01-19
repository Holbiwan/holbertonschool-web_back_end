export default class Currency {
    constructor(code, name) {
        this._code = code;
        this._name = name;
    }
    
    get code() {
        return this._code;
    }
    
    // code
    set code(code) {
        if (typeof code === 'string') {
        this._code = code;
        } else {
        throw new TypeError('Code must be a string');
        }
    }
    
    // name
    get name() {
        return this._name;
    }
    
    set name(name) {
        if (typeof name === 'string') {
        this._name = name;
        } else {
        throw new TypeError('Name must be a string');
        }
    }
    
    // displayFullCurrency
    displayFullCurrency() {
        return `${this._name} (${this._code})`;
    }
    }
