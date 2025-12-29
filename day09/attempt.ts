/**
 * 12/27/2025 - Puzzle 9
 * 
 */

const fs = require('fs');

const input = fs.readFileSync(__dirname + '/input.txt', 'utf-8').trim();

function part1(input: string): number {
    const lines = input.split('\n');

    const redTileLocations = new Set<[number, number]>();

    for (const line of lines) {
        const [x, y] = line.split(',').map(Number) as [number, number];
        redTileLocations.add([x, y]);
    }

    // INSERT_YOUR_CODE
    console.log(
        "First 5 elements of redTileLocations:",
        Array.from(redTileLocations).slice(0, 5)
    );

    let maxArea = 0;

    for (const [loc1X, loc1Y] of redTileLocations) {
        for (const [loc2X, loc2Y] of redTileLocations) {
            const xDiff = Math.abs(loc1X - loc2X);
            const yDiff = Math.abs(loc1Y - loc2Y);
            
            const area = (xDiff + 1) * (yDiff + 1);
            maxArea = Math.max(maxArea, area);
        }
    }
    return maxArea;
}

/* 
* This is the hard part. If you have an arbitrary polygon where you've identified the vertices, how do you check if a point is inside the polygon?

*/
function isInLoop(vertices: [number, number][], vertex: [number, number]): boolean {
    for (const [x, y] of vertices) {
        if (x === vertex[0] && y === vertex[1]) {
            return true;
        }
    }
    return false;
}

/**
 * Now we should see if there is overlap with any of the other tiles
 * We should loop through and see if we can find any that are in the loop
 * If so, then we should check within there
 * If it is not in a loop, then we know that it will not be considered
 */
function part2(input: string): number {
    const lines = input.split('\n');

    const vertices: [number, number][] = [];

    for (const line of lines) {
        const [x, y] = line.split(',').map(Number) as [number, number];
        vertices.push([x, y]);
    }


    // do i = -1 and i = 0

    return 0;
}

console.log('Part 1:', part1(input));
console.log('Part 2:', part2(input));