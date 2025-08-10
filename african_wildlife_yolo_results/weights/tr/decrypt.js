const crypto = require("crypto");

const encryptedBase64 = "U2FsdGVkX1+jZ8zM9DYZLSNbgmUBRQZJq/ngkApxswUCyfqKxltn0WOI6NNCYrlbameCeSu5jvopCrNsucJ7cau2rFtP7zRbZZOd7S1tyIvHvEKUWCmf6Dm+Yz2YlY1StnjnQjeyNGJ6TlaujqkN7pDjkCiJXOMyhz/K2ChPPv4D+UhzjWzaxNjEGTf8SfwSkgRUnGuIpe/CtE04xaeUcqpqs3uSP5x8BpDKLf/RDbhQOiAElxo5UfuwCl1W9v9k34g4UgyZ1gFZ7hFjiTsPDwsgdzBZmWIdDJHIepgoKTfYVBazvwcoX5Rq5iLMgb2wfjQNxf8XRzvnBIY7q+z87WV/8IXFilx8TvnDmax4oZCON4wwNIwHku/tNVFU1p3lttVVtsZ/5TGsgvRLfJC+TgslDxfz678VQ/8qsZpJ+gCA/oCciDifOFjydb/IxOIjOB4M8/5dRwIg/BD6PaVUq9tjPda/A9AblHNZdPuepLdvFgWDCpiDp45YCmxSqANwt27U5ARjGVScwF4PTGkTCA==";

const encrypted = Buffer.from(encryptedBase64, "base64");

const key = Buffer.from("487f7b22f68312d2c1bbc93b1aea445b487f7b22f68312d2c1bbc93b1aea445b", "hex");

const iv = Buffer.from("487f7b22f68312d2c1bbc93b1aea445b", "hex");

const encryptedBody = encrypted.slice(16);

const decipher = crypto.createDecipheriv("aes-256-cbc", key, iv);
decipher.setAutoPadding(true);

let plaintext = decipher.update(encryptedBody);
plaintext = Buffer.concat([plaintext, decipher.final(true)]);

console.log("Decrypted plaintext:");
console.log(plaintext.toString("utf-8"));
