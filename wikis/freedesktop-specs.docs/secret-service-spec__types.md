## 14 Types

[14.1 Struct types](types.md#id-1.3.4.2)

[14.2 Map types](ch14s02.md)

## 14.1 Struct types

### 14.1.1 `Secret`

The Secret type holds a (possibly encoded) secret.

Arrays of Secret don't generally make sense.

``` classsynopsis
 struct Secret {
  ObjectPath session ;
  Array<Byte> parameters ;
  Array<Byte> value ;
  String content_type ;
}
```

`session`  
The session that was used to encode the secret.

`parameters`  
Algorithm dependent parameters for secret value encoding.

`value`  
Possibly encoded secret value

`content_type`  
The content type of the secret. For example: 'text/plain; charset=utf8'
