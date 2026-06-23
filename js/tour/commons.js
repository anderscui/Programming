'use strict';

// const commons = {
//     print(obj) {
//         console.log(obj);
//     },

//     printObject(obj) {
//         for (const [key, value] of Object.entries(obj)) {
//             console.log(`${key}: ${value}`);
//         }
//     }
// }

// debugging
function print(obj) {
    console.log(obj);
}

function printObject(obj) {
    for (const [key, value] of Object.entries(obj)) {
        console.log(`${key}: ${value}`);
    }
}

// random
function random(min, max) {
    return Math.random() * (max - min) + min;
}

function randomInteger(min, max) {
    let rand = Math.random() * (max + 1 - min) + min;
    return Math.floor(rand);
}

function choice(items) {
    return items[
        randomInteger(0, items.length - 1)
    ];
}

// arrays
// function uniqueArray(arr) {
//     let found = new Set();
//     let filtered = [];
//     for (let elem of arr) {
//         if (found.has(elem)) {
//             continue;
//         }
//         filtered.push(elem);
//         found.add(elem);
//     }
//     return filtered;
// }

function uniqueArray(arr) {
  return Array.from(new Set(arr));
}

// assertion
function assert(condition, message = 'Assertion failed') {
    if (!condition) {
        throw new Error(message);
    }
}

function assertNot(condition, message = 'Assertion failed') {
    assert(!condition, message);
}

function assertEqual(expected, actual, message = 'Assertion failed') {
    if (expected !== actual) {
        print(`expected: ${expected}, actual: ${actual}`);
        throw new Error(message);
    }
}

function assertArrayEqual(expected, actual, message = 'Assertion failed') {
    if (!Array.isArray(expected) || !Array.isArray(actual)) {
        throw new Error('Two arrays are expected.');
    }

    if (expected.length !== actual.length) {
        throw new Error(message + `: diff length (${expected.length} vs. ${actual.length})`);
    }

    for (let i = 0; i < expected.length; i++) {
        if (expected[i] !== actual[i]) {
            throw new Error(`${message}: diff element at ${i}: expected: ${expected[i]}, actual: ${actual[i]}`);
        }
    }
}
