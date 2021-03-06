function countingValleys(steps, path) {
    
    let valleys = 0
    let sealevel = 0

    for (let i = 0; i < steps; i++) {
        if (path[i] === 'D') {
            sealevel--
        } 
        if (path[i] === 'U') {
            sealevel++
        }
        if (sealevel === 0 && path[i] === 'U') {
            valleys++
        }
    }

    return valleys
}

console.log(countingValleys(12, 'DDUUDDUDUUUD'))
console.log(countingValleys(8, 'UDDDUDUU'))