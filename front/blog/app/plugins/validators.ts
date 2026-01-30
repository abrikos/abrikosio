export default defineNuxtPlugin(() => {
  return {
    provide: {
      email: [(val: string) => (val && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val)) || 'Wrong email'],
      required: [(val: string) => val && val.length >0  || 'Field required'],
    }
  }
})
