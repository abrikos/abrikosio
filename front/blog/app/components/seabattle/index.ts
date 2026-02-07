export interface ICell {
    row: number
    col: number
    index?: number
    ship?: number
    horizontal?: boolean
    isShip?: boolean
    strike?: boolean
    hit?: boolean
    kill?: boolean
}

export interface ISeaBattle {
    rows: number
    cols: number
    id: number
    field_my: ICell[]
    field_op: ICell[]
    field_op_masked: ICell[]
    is_active?: boolean
}
