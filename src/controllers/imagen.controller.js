import AWS from 'aws-sdk';

export const generarURLFirmada = async (req, res) => {
  const s3 = new AWS.S3()
  const data = req.body
  console.log(data)
  // putObject sirve para indiciar que la url generada se usar para subir un archivo
  // getObject
  const url = s3.getSignedUrl('putObject', {
      Bucket: process.env.BUCKET_NAME,
      Key: data.nombreArchivo,
      Expires: 60, // El valor es en numeros y representa la cantidad de segundas que sera valida
      // Tipo de archivo que vamos a subir
      ContentType: data.contentType,
  });
  
  return res.json({
      content: url,
  });
};