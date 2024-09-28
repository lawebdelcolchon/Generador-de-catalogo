<?php
require 'vendor/autoload.php';

use Dompdf\Dompdf;

// Inicializar Dompdf
$dompdf = new Dompdf();

// Cargar el contenido HTML
$html = file_get_contents('catalogo.html');

// Cargar el HTML al Dompdf
$dompdf->loadHtml($html);

// (Opcional) Configurar tamaño y orientación del papel
$dompdf->setPaper('A4', 'portrait');

// Renderizar el PDF
$dompdf->render();

// Salida del PDF al navegador
$dompdf->stream("catalogo.pdf", ["Attachment" => true]);
?>
