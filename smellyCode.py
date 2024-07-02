def add(a, b) {
    return (a + b)
}

def add(int[] a) {
    int answer = 0
    for x in a:
        answer = add(answer, x)
}