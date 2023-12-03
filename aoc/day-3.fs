open System.IO
open System.Text.RegularExpressions
open System

let readLines (filePath: string) =
    seq {
        use sr = new StreamReader(filePath)

        while not sr.EndOfStream do
            yield sr.ReadLine()
    }

let rec to2dArray (list: list<string>, arr: array<array<char>>) =
    match list with
    | [] -> arr
    | h :: t ->
        let charArr = [| h.ToCharArray() |]
        let newArray = Array.append arr charArr
        to2dArray (t, newArray)

let chechIfValidNumber (m: Match, engineMap: array<array<char>>, lineIndex: int, len: int) =
    let lenTemp = len - 1
    let startLine = if (lineIndex = 0) then 0 else lineIndex - 1
    let endLine = if (lineIndex = lenTemp) then lineIndex else lineIndex + 1
    let startIndex = if (m.Index = 0) then 0 else m.Index - 1

    let endIndex =
        if ((m.Index + m.Length - 1) = 139) then
            139
        else
            m.Index + m.Length

    let indexArr = [| for i in startIndex..endIndex -> i |]
    let lineArr = [| for i in startLine..endLine -> i |]
    let mutable isValid = false

    for line in lineArr do
        for index in indexArr do
            if
                (engineMap[line][index] <> '.'
                 && Char.IsAsciiDigit(engineMap[line][index]) <> true)
            then
                isValid <- true
                true
            else
                false

    isValid

let rec calculateValidNumbersSum (m: list<Match>, engineMap: array<array<char>>, lineIndex: int, len: int, sum: int) =
    match m with
    | [] -> sum
    | h :: t ->
        let isValid = chechIfValidNumber (h, engineMap, lineIndex, len)
        let partialSum = if (isValid) then int (h.Value) else 0
        calculateValidNumbersSum (t, engineMap, lineIndex, len, sum + partialSum)

let rec caluclateEngineSum (list: list<string>, sum: int, engineMap: array<array<char>>, id: int, len: int) =
    match list with
    | [] -> sum
    | h :: t ->
        let numbersMatches = Regex.Matches(h, @"(\d+)") |> Seq.cast

        let lineSum =
            calculateValidNumbersSum (Seq.toList (numbersMatches), engineMap, id, len, 0)

        caluclateEngineSum (t, sum + lineSum, engineMap, id + 1, len)


let dayInput = readLines ("./day-3.txt")
let engineMap = to2dArray (Seq.toList (dayInput), Array.empty)

let sum =
    caluclateEngineSum (Seq.toList (dayInput), 0, engineMap, 0, Seq.toList(dayInput).Length)

Console.WriteLine(sprintf "%A" sum)
