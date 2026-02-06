export interface ICell {
    row: number
    col: number
    index?: number
    ship?: number
    horizontal?: boolean
    isShip?: boolean
}

export interface ISeaBattle {
    rows: number
    cols: number
    field_my: ICell[]
    field_op: ICell[]
}

// export function getIndex(game:ISeaBattle, cell: ICell) {
//     return (cell.row) * game.cols + cell.col
// }
//
// function cellIsFree(game:ISeaBattle, cell: ICell) {
//     return cell.row +1 <game.rows && cell.col +1 < game.cols
// }
//
// export function validateCell(game:ISeaBattle, args: ICell): boolean {
//     if (!args.ship) return false
//     const shipCells = prepareShipCells(args)
//
//     for (const ship of shipCells) {
//         if (!cellIsFree(game, ship)) return false
//         if (cell.ship) return false
//     }
//     return !!shipCells.length
// }

//
// export function placeShip(field:ICell[], args: ICell) {
//     //if (!validateCell(field, args) || !args.ship) return
//
//     const cell = getCell(field, args)
//     if (!cell) return
//
//     const shipCells = prepareShipCells(args)
//     if (!shipCells) return
//     for (const shipCell of shipCells) {
//         const cell = getCell(field, shipCell)
//         cell && (cell.isShip = true)
//     }
//     for (const ship of shipCells) {
//         for (let row = ship.row - 1; row <= ship.row + 1; row++) {
//             for (let col = ship.col - 1; col <= ship.col + 1; col++) {
//                 const cell = getCell(field, {row, col})
//                 if (!cell) continue
//                 cell.ship = args.ship
//             }
//         }
//     }
// }

export function prepareShipCells(game: ISeaBattle, args: ICell): ICell[] {
    if (!args.ship) return []

    const ship = []

    if (args.horizontal) {
        for (let col = args.col; col < args.col + args.ship; col++) {
            if (col >= game.cols) continue
            const index = (args.row) * game.cols + col
            ship.push({...args, col, isShip: true, index})
        }
    } else {
        for (let row = args.row; row < args.row + args.ship; row++) {
            if (row >= game.rows) continue
            const index = row * game.cols + args.col
            ship.push({...args, row, isShip: true, index})
        }
    }
    return ship;
}

// export function getCell(field: ICell[], cell: ICell) {
//     return field.find(c => c.col === cell.col && c.row === cell.row)
// }

export function getRowColByIndex(game: ISeaBattle | undefined, index: number) {
    if (!game) return {}
    return {
        row: Math.floor(index / game.cols),
        col: index % game.rows,
        index
    }
}

//
// export function defaultField(rows: number, cols: number) {
//     return Array.from(Array(rows * cols).keys())
// }