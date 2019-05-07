#r "Newtonsoft.Json"

using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using System.Globalization;
using Newtonsoft.Json;
using System;
using System.Text;
using System.Net;
using System.Net.Http.Headers;

public static async Task<HttpResponseMessage> Run(HttpRequest req, TraceWriter log)
{
    int lact_n = 0, lbd_d = 0;
    float daily_prod = 0.0F, lact_d = 0.0F;

    try {
        Int32.TryParse(req.Query["lact_n"], out lact_n);
        Int32.TryParse(req.Query["lbd_d"], out lbd_d);
    
        daily_prod = float.Parse(req.Query["daily_prod"], CultureInfo.InvariantCulture.NumberFormat);
        lact_d = float.Parse(req.Query["lact_d"], CultureInfo.InvariantCulture.NumberFormat);
    } catch(Exception e) {
        Console.WriteLine("Error occured in parsing data");
    }    
    
    Dictionary<string, float> dictionary = new Dictionary<string, float>();
    dictionary.Add("daily_prod", daily_prod);
    dictionary.Add("lact_d", lact_d);
    dictionary.Add("lact_n", lact_n);
    dictionary.Add("lbd_d", lbd_d);
    
    string json = JsonConvert.SerializeObject(dictionary);
    
    string trigger_url = "http://52.151.237.207:80/score";
    string res = "";
    using(var client = new HttpClient()) {
        var content = new StringContent(json, Encoding.UTF8, "application/json");
        var result = await client.PostAsync(trigger_url, content);
        res = await result.Content.ReadAsStringAsync();
    }

    log.Info($"req:{req.ToString()}, response:{res}");

    var response = new HttpResponseMessage(HttpStatusCode.OK) {
        Content = new StringContent(JsonConvert.SerializeObject(res.ToString()), Encoding.UTF8, "application/json")
    };
    return response;
}