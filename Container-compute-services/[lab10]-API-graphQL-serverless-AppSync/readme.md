
 architecture
                     
       s3(index.html)----> appSync(API GraphicQL) ----> DynamoDB(Users)

✅ Créer un backend GraphQL avec AWS AppSync.
✅ Configurer DynamoDB comme source de données.
✅ Tester les requêtes et mutations GraphQL.
✅ Créer une interface Web pour interagir avec l’API (S3 Static Website).


6fbb523b-34c4-499d-a0e8-db86115b375b

add

export function request(ctx) {
  return {
    operation: 'PutItem',
    key: {
      // Automatically generates a cryptographically secure UUID v4
      user_id: util.dynamodb.toDynamoDB(util.autoId()), 
    },
    attributeValues: {
      name: util.dynamodb.toDynamoDB(ctx.args.name),
      email: util.dynamodb.toDynamoDB(ctx.args.email),
    },
  };
}


get 

export function request(ctx) {
  return {
    operation: 'GetItem',
    key: {
      // Ensure it is explicitly converted to a DynamoDB String Attribute
      user_id: util.dynamodb.toDynamoDB(ctx.args.user_id),
    },
  };
}


✅ API GraphQL Serverless avec AWS AppSync.
✅ DynamoDB comme backend NoSQL.
✅ Interface web statique sur S3 pour tester l’API.