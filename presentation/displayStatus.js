window.addEventListener('load', () => {
    const output = document.getElementById('output')

    const log = (message, color) => {
        const line = document.createElement('div');
        line.style.color = 'white'
        line.style.backgroundColor = color
        line.style.margin = '1px'
        line.style.padding = '3px'
        line.style.fontFamily = 'Monospace'
        line.appendChild(document.createTextNode(message))
        output.appendChild(line)
    }

    if (!window.testStatus) {
        return
    }

    window.testStatus.reverse().forEach(entry => {
        log(entry.message, entry.type === 'PASS' ? 'green' : 'red')
    })

})