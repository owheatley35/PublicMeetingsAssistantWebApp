function formatDateForPresentation(inputString: string): string {
    const splitDate = inputString.split('-')
    return `${splitDate[2]}/${splitDate[1]}/${splitDate[0]}`
}

export default formatDateForPresentation
