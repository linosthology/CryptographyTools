// Extended Euclidian Algorithm

extendedEucildianAlgorithm = (modulus, numberToInverse) => {
    steps = []
    steps = firstStep(modulus, numberToInverse, steps)

    console.log()
    console.log(steps)
    console.log()

    inverse = calculateInverse(steps, modulus)
    console.log('\nThe Inverse of ' + numberToInverse + ' is ' + inverse + '\n')
}

firstStep = (modulus, numberToInverse, steps) => {
    continues = true
    while (continues) {
        returnValue = numberToInverse
        i = 0
        while (returnValue <= modulus) {
            if (numberToInverse === 0) {
                break
            } else if (numberToInverse * i <= modulus) {
                returnValue = numberToInverse * i
                if (numberToInverse * (i + 1) <= modulus) {
                    i++
                } else {
                    break
                }
            } else {
                break
            }
        }

        if (numberToInverse !== 0) {
            steps.push([modulus, numberToInverse])
            modulus = modulus % returnValue
            firstStep(numberToInverse, modulus, steps)
            save = modulus
            modulus = numberToInverse
            numberToInverse = save
        } else {
            steps.push([modulus, numberToInverse])
            continues = false
        }
    }
    return steps
}

calculateInverse = (steps, modulus) => {
    trash = steps.pop()
    trash = steps.pop()

    continues = true
    multiplier = 1
    currentStep = steps.pop()
    product = 0
    while (continues) {
        product = currentStep[0] * multiplier
        multiplier = (1 - product) / currentStep[1]
        console.log(`${product} + ${currentStep[1]} + (${multiplier}) = 1`)
        if (steps.length > 0) {
            currentStep = steps.pop()
        } else continues = false
    }
    return (currentStep[0] + multiplier) % modulus
}

// mod, numberToInverse
extendedEucildianAlgorithm(15, 11)
