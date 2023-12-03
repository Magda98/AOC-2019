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

// number is valid when is adjacent to a symbol except `.` (period)
let chechIfValidNumber (matchGroup: Match, engineMap: array<array<char>>, lineIndex: int, listLenght: int) =
    let listMaxIndex = listLenght - 1
    let startLine = if (lineIndex = 0) then 0 else lineIndex - 1

    let endLine =
        if (lineIndex = listMaxIndex) then
            lineIndex
        else
            lineIndex + 1

    let startIndex = if (matchGroup.Index = 0) then 0 else matchGroup.Index - 1

    let endIndex =
        if ((matchGroup.Index + matchGroup.Length - 1) = 139) then
            139
        else
            matchGroup.Index + matchGroup.Length

    let indexArr = [| for i in startIndex..endIndex -> i |]
    let lineArr = [| for i in startLine..endLine -> i |]

    let isInvalid =
        Array.forall
            (fun line ->
                Array.forall
                    (fun index -> engineMap[line][index] = '.' || Char.IsAsciiDigit(engineMap[line][index]))
                    indexArr)
            lineArr

    not isInvalid

let rec calculateValidNumbersSum
    (
        m: list<Match>,
        engineMap: array<array<char>>,
        lineIndex: int,
        listLength: int,
        sum: int
    ) =
    match m with
    | [] -> sum
    | h :: t ->
        let isValid = chechIfValidNumber (h, engineMap, lineIndex, listLength)
        let partialSum = if (isValid) then int (h.Value) else 0
        calculateValidNumbersSum (t, engineMap, lineIndex, listLength, sum + partialSum)

let rec caluclateEngineSum (list: list<string>, sum: int, engineMap: array<array<char>>, id: int, len: int) =
    match list with
    | [] -> sum
    | h :: t ->
        let numbersMatches = Regex.Matches(h, @"(\d+)") |> Seq.cast

        let lineSum =
            calculateValidNumbersSum (Seq.toList (numbersMatches), engineMap, id, len, 0)

        caluclateEngineSum (t, sum + lineSum, engineMap, id + 1, len)


let dayInput = readLines ("./day-3.txt")
let dayInputList = Seq.toList (dayInput)
let engineMap = to2dArray (Seq.toList (dayInput), Array.empty)

let sum = caluclateEngineSum (dayInputList, 0, engineMap, 0, dayInputList.Length)

Console.WriteLine(sprintf "%A" sum)
