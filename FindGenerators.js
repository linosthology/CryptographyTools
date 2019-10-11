findGenerators = mod => {
    // list for all the elements
    zElements = getElements(mod)
    console.log('\nall Elements in Group\n', zElements)

    // coprime Sorting
    coprimeSorted = coprimeSort(mod, zElements)
    console.log('\nelements coprimeSorted\n', coprimeSorted)

    // finding the Generators
    generators = []
    generators = getGenerators(mod, coprimeSorted)
    console.log('\ngenerators of the group\n', generators)

    console.log()
}

getElements = mod => {
    zElements = []
    for (i = 1; i < mod; i++) zElements.push(i)
    return zElements
}

coprimeSort = (mod, zElements) => {
    coprimeSorted = []

    zElements.forEach(element => {
        commonDivider = false
        for (i = 2; i <= element; i++) {
            if (element % i === 0 && mod % i === 0) {
                commonDivider = true
            }
        }

        if (!commonDivider) {
            coprimeSorted.push(element)
        }
    })

    return coprimeSorted
}

getGenerators = (mod, coprimeSorted) => {
    return coprimeSorted
}

findGenerators(6)
