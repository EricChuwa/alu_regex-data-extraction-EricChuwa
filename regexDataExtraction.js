/** Regex Patterns */
const emailRegex = /\b[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b/g;
const urlRegex = /https?:\/\/[a-zA-Z0-9._]+\.[a-zA-Z]{2,}([\/\w /-]*)?/g;
const phoneNumberRegex = /\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}/g;
const creditCardNumberRegex = /\d{4}?[\s.-]?\d{4}?[\s.-]?\d{4}?[\s.-]?\d{4}/g;
const timeRegex = /\b([01]?[0-9]|2[0-3]):[0-5][0-9](\s?(AM|PM))?\b/gi;
const htmlTagRegex = /\<[a-zA-Z0-9]+\>/g;
const hastagRegex = /#[a-zA-Z0-9_]+/g;
const currencyRegex = /\$[0-9]+\,?[0-9]+?\.[0-9]/g;

text = "01202301236 afaefwefaefafafed"

pn = text.match(phoneNumberRegex)
console.log(pn)