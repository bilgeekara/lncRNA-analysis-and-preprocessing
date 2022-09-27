# import libraries
from pyensembl import EnsemblRelease


class Transcripts:
    
    """
    A customized class from pyensembl modules
    """
    
    def __init__(self) -> None:
        """
        a trancript object that can be manipulated
        """
        
        self.data = EnsemblRelease(release=106)
        
        
    def extract_info(self,Transcript_object):
        """
        extract the essential coordinate info from a given transcript object and returns
        """
        
        extract = {}
        
        extract["contig"] = Transcript_object.contig # chromosome type
        extract["start"] = Transcript_object.start
        extract["end"] = Transcript_object.end
        extract["strand"] = Transcript_object.strand # forward strand(+) reverse strand (-)
        extract["transcript_name"] = Transcript_object.name
        extract["gene_id"] = Transcript_object.gene_id
        extract["biotype"] = Transcript_object.biotype # coding or non-coding
        
        return extract
    
    
    def map_transcript_ids(self,transcript_ids):
        """
        map a list of transcipt ids to their genomic coordinates
        return (raw_coordinates, arranged_coordinates)
            raw coordinates contain all the transcript entities: name, start, end, contig, strand, etc
            arranged_coordinates coordinates contain the chromosome number, strand, start and end positions 
            as such:'Chromosome 6+: 75749239:75919537' 
        """

        raw_coordinates = {}
        arranged_coordinates = {}

        # load the ensembl release data

        for transcript_id in transcript_ids:
            # create a transcript object for the given transcript id
            try:
                Transcript_object = self.data.transcript_by_id(transcript_id = transcript_id)
            except:
                continue

            # extract coordinates from transcript object
            extract = self.extract_info(Transcript_object)

            # record raw coordinates
            raw_coordinates[transcript_id] = extract

            # arrange coordinates into a single string 
            coordinates = f'Chromosome {extract["contig"]}{extract["strand"]}: {extract["start"]}:{extract["end"]}'

            # record arranged coordinates
            arranged_coordinates[transcript_id] = coordinates
        return raw_coordinates, arranged_coordinates