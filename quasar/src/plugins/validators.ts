export default {
  email: [(val: string) => (val && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val)) || 'Wrong email'],
};
