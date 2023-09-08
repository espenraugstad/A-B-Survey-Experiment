import { randomUUID } from "crypto";
import { DynamoDBClient, PutItemCommand } from "@aws-sdk/client-dynamodb";

export const handler = async (event) => {
  
  let now = new Date();
  let timestamp =
    now.toLocaleDateString("no-NB") + " " + now.toLocaleTimeString("no-NB");
    
  const id = randomUUID();
    
  const client = new DynamoDBClient({region: "eu-north-1"});
  const input = {
    "Item": {
      "id": {
        "S": id
      },
      "timestamp": {
        "S": timestamp
      },
      "cola": {
        "S": event.cola
      },
      "variant": {
        "S": event.variant
      }
    },
    "TableName": "MySurveyResults",
  };
  
  const command = new PutItemCommand(input);
  const response = await client.send(command);
  
  return response;
};