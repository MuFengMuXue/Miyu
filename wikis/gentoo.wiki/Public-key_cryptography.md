**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Public-key_cryptography "wikipedia:Public-key cryptography")

Public-key cryptography allows for the exchange of confidential information between two parties, without having an initially agreed upon encryption key (which would fall onto symmetric encryption). Instead, each party has a publicly available key and a private key. With the public key, other people can encrypt information which only the private key (associated with the public key) can decrypt.

## Contents

-   [[1] [The world of public key cryptography]](#The_world_of_public_key_cryptography)
    -   [[1.1] [The math behind the idea]](#The_math_behind_the_idea)
    -   [[1.2] [Signatures]](#Signatures)
    -   [[1.3] [Key servers and signed keys]](#Key_servers_and_signed_keys)

## [The world of public key cryptography]

The concept of public key cryptography was originally devised by Whitfield Diffie and Martin Hellman in 1976. When I first heard the words \"public key\" and \"cryptography\" in the same sentence back in \'93 I thought to myself that it would be impossible to do such a thing. In those days there was no Internet (well there was, but not for me) so I went to the public library and asked for books on Cryptography. I must say that I was 16 at the time so the clerk there looked to me in astonishment and brought me a book for children on substitution cyphers (those where you change a letter for another like the famous Caesar Cypher or ROT-13 (Tragbb Ebpxf, naq lbh xabj vg vf tbbq orpnhfr lbh ner ernqvat guvf qbp.), `emerge rotix` if the preceding text not be read). I was very upset with this and started to search for more info. It is good to have mathematicians in the family, because as soon as I talked to one of them I was introduced to a new world.

### [The math behind the idea]

And now a bit of mathematics:

[CODE] **Mathematical Concepts**

    Definitions:

    1- A prime number is a positive integer number greater than one that is only
    divisible by 1 and itself (the remainder of the division is 0).
    The first 8 prime numbers are 2,3,5,7,11,13,17,19

    Theorem (No proof here)
    1- For any non prime positive integer it is possible to break it as the product
    of prime numbers, and that product is unique.
    4=2*2
    6=2*3
    8=2*4=2*2*2
    10=2*5
    12=2*6=2*2*3

    "Facts":
    1- It is mathematically easy to multiply two large integers.
    2- It is hard to find the prime factors of a given positive integer.

If I give you the number 35 and I tell you that this number is the product of two prime numbers it is easy to find that it was 5 and 7. But if I tell you the same for 1588522601 you will spend a lot of time (or CPU cycles) to find it was 49811\*31891. And if this number is really really big this task becomes \"impossible\". So now if I give the world my large number that is the product of two primes I know something about that number that no one else knows.

This is the basis for Public Key Cryptography (PKC) implementations today. As an (unrealistic) example, I give anyone my number and that someone will use if for cyphering a message to me. Anyone can see the cyphered message, because I am the only one who knows a shortcut to read it, anyone else will first have to \"split\" that big number to be able to read the message, and it is a \"fact\" that it is impossible to do that in a short amount of time (today\'s methods and the fastest computers in the world would take thousands of years to do that). In this setup the two large prime numbers would be called the PRIVATE KEY, and the large non prime number is the PUBLIC KEY.

In practice this is not 100% accurate with reality, but will give a good idea to the newcomer. For more information, check Wikipedia on the [Diffie-Hellman](https://en.wikipedia.org/wiki/Diffie-Hellman) protocol. For even more info go to the public library and grab a copy of the [\"Handbook of Applied Cryptography\"](http://www.cacr.math.uwaterloo.ca/hac/) by Alfred J. Menezes, Paul C. van Oorschot and Scott A. Vanstone. This book is also available online for free at the above site.

One consequence of the above is that if you cypher a message to me, and you loose the original uncyphered message you will no longer be able to retrieve it from the cyphered version.

### [Signatures]

From this article it is possible to see how a user can send a cyphered message if they have a public key, but how does one know that the author of the message is really who they claim to be? Or in other words: If Larry receives an email from Luic how do I really know it was you and not someone else claiming to be you?

Remember me saying that PKC was not as simple as I had said? The idea is that when you cypher a message to me you sign it with your private key so that, when I receive it, I can first use your public key to check your signature and then use my private key to decypher the message. As you can see we could not do that in the setup I described before.

It\'s also very important to sign messages so that you don\'t have to cypher them beforehand. Now you can create messages that can be read by anyone, but that come with your \"branding\". And if any single character is changed in the message it can (and will) be detected.

### [Key servers and signed keys]

But let\'s say that I have no previous contact with you until you send me a message: how do I get your public key, and how do I really know it is yours?

To solve this problem public Key Servers were created. When you create your key pair (Public and Private key), you send your public key to the key server. After this everyone can retrieve your key from there. This solves the problem of finding the key. But how do I really know that that key is the author\'s key? For this another concept must be introduced, and that is key signing:

Key signing means that if I have the public key of another person, and I know *for sure* that it is really that persons key (it is my personal friend, someone I know in real life, etc.) I can sign that public key and send it to key servers, that way I am telling the world: \"This key really belongs to the person it claims to belong.\". That way persons that have my public key and trust me can use that trust to trust other keys.

This can sometimes be confusing so lets see a real world situation.

Let\'s imagine a 3 person situation: John, Mary, and Lisa. John is a good friend of Mary but does not know Lisa; Lisa is a good friend of Mary but does not know John. One day Lisa sends John a signed email. John will fetch Lisa\'s Public Key from the key server and test the message, if all went ok he will see that whoever wrote that message also created that key. But how do I know it was really the person it claims to be?

He then sees that it is signed by Mary, which he can check because he already has Mary\'s key and he trusts that key. With this ring of trust he continues to conclude that the email he received was really written by Lisa.