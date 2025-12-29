/**
 * 12/29/2025 - Puzzle 7
 * 
 */

const fs = require('fs');

const input = fs.readFileSync(__dirname + '/input.txt', 'utf-8').trim();

function part1(input: string): number {
    const lines = input.split('\n');

    let splitterIndexes: Set<number> = new Set();
    splitterIndexes.add(lines[0]?.indexOf('S') as number);


    let numSplits = 0;
    for (let i = 1; i < lines.length; i++) {
        const line = lines[i] as string;
        let newSplitterIndexes: Set<number> = new Set();
        for (let splitterIndex of splitterIndexes) {

            if (line[splitterIndex] === '^') {
                numSplits++;
                newSplitterIndexes.add(splitterIndex - 1);
                newSplitterIndexes.add(splitterIndex + 1);
            } else { // == '.'
                newSplitterIndexes.add(splitterIndex);
            }
        }
        splitterIndexes = new Set(newSplitterIndexes);
    }

    return numSplits;
}

function part2(input: string): number {
    const lines = input.split('\n');

    let splitterIndexWithNumTimelines: Map<number, number> = new Map();
    splitterIndexWithNumTimelines.set(lines[0]?.indexOf('S') as number, 1);

    for (let i = 1; i < lines.length; i++) {
        const line = lines[i] as string;
        let newSplitterIndexesAndNumTimelines: Map<number, number> = new Map();
        for (let [splitterIndex, numTimelines] of splitterIndexWithNumTimelines) {

            if (line[splitterIndex] === '^') {
                let leftIndex = splitterIndex - 1;
                let rightIndex = splitterIndex + 1;
                newSplitterIndexesAndNumTimelines.set(leftIndex, (newSplitterIndexesAndNumTimelines.get(leftIndex) || 0) + numTimelines);
                newSplitterIndexesAndNumTimelines.set(rightIndex, (newSplitterIndexesAndNumTimelines.get(rightIndex) || 0) + numTimelines);
            } else { // == '.'
                newSplitterIndexesAndNumTimelines.set(splitterIndex, (newSplitterIndexesAndNumTimelines.get(splitterIndex) || 0) + numTimelines);
            }
        }
        splitterIndexWithNumTimelines = new Map(newSplitterIndexesAndNumTimelines);
    }

    return Array.from(splitterIndexWithNumTimelines.values()).reduce((acc, curr) => acc + curr, 0);
}

console.log('Part 1:', part1(input));
console.log('Part 2:', part2(input));