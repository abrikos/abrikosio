import moment from 'moment'
export default defineNuxtPlugin(() => {
    return {
        provide: {
            priceFormat: (value: number) => {
                return value && value.toFixed(2).replace(/(\d)(?=(\d{3})+([^\d]|$))/g, '$1 ')
            },
            getMonthName: (monthNumber: number) => {
                // Create a date object. We can use any year, day, and time.
                // We subtract 1 from monthNumber because JavaScript months are 0-based.
                const date = new Date(2000, monthNumber - 1, 1);

                // Use toLocaleString to get the month name in a specific locale
                return date.toLocaleString('ru-RU', {month: 'long'});
                // For a short name, use { month: 'short' } (e.g., "Jan")
            }
        }
    }
})