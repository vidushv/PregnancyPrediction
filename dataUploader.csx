#r "Newtonsoft.Json"

using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using System.Globalization;


public static IActionResult Run(HttpRequest req, out object taskDocument, ILogger log)
{
    int lact_n = 0, lbd_d = 0, label = 0, ID=0;
    float daily_prod = 0.0F, lact_d = 0.0F;
    
    try {
        Int32.TryParse(req.Query["lact_n"], out lact_n);
        Int32.TryParse(req.Query["lbd_d"], out lbd_d);
        Int32.TryParse(req.Query["ID"], out ID);
        Int32.TryParse(req.Query["label"], out label);
        
        daily_prod = float.Parse(req.Query["daily_prod"], CultureInfo.InvariantCulture.NumberFormat);
        lact_d = float.Parse(req.Query["lact_d"], CultureInfo.InvariantCulture.NumberFormat);
    } catch(Exception e) {
        Console.WriteLine("Error occured in parsing data");
    }
    
    Console.WriteLine(req);
    // We need both ID and label parameters.
    // if (!string.IsNullOrEmpty(ID) && !string.IsNullOrEmpty(PREG))
    //{
    taskDocument = new {
            ID,
            lbd_d,
            lact_n,
            lact_d,
            daily_prod,
            label
        };

    return (ActionResult)new OkResult();
    //}
    // else
    //{
    //    taskDocument = null;
    //    return (ActionResult)new BadRequestResult();
    //}
}